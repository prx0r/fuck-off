import { useState, useCallback } from "react";

const C = {
  bg: "#07090f", card: "#0f1319", cardHover: "#161d27", border: "#1c2333",
  borderHi: "#3b82f6", text: "#e2e8f0", muted: "#94a3b8", dim: "#546178",
  blue: "#3b82f6", green: "#10b981", red: "#ef4444", amber: "#f59e0b",
  purple: "#8b5cf6", cyan: "#06b6d4", pink: "#ec4899",
  greenBg: "rgba(16,185,129,.12)", redBg: "rgba(239,68,68,.12)", amberBg: "rgba(245,158,11,.12)", blueBg: "rgba(59,130,246,.12)",
};

const now = Date.now();
const CHECKPOINTS = [
  { id:"cp-a1b2c3", ts:now-50000, status:"active", branch:"main", path:["task_intake"], desc:"Task received — Analyze Q4 earnings", state:{task:"Analyze Q4 earnings",status:"received"}, meta:{confidence:1,tokens:0}, parent:null },
  { id:"cp-d4e5f6", ts:now-42000, status:"active", branch:"main", path:["task_intake","planning"], desc:"Created 4-step execution plan", state:{plan:["Retrieve data","Extract metrics","Compare QoQ","Summarize"],step:1}, meta:{confidence:.92,tokens:150}, parent:"cp-a1b2c3" },
  { id:"cp-g7h8i9", ts:now-35000, status:"rolled_back", branch:"main", path:["task_intake","planning","retrieve:fail"], desc:"API timeout — 503 Service Unavailable", state:{error:"API 503",step:1}, meta:{confidence:.2,tokens:200,error:true}, parent:"cp-d4e5f6" },
  { id:"cp-j1k2l3", ts:now-28000, status:"active", branch:"cached-path", path:["task_intake","planning","use_cache"], desc:"Branch: Using cached financial data", state:{approach:"cached_data",source:"local_cache",revenue:"$12.4B"}, meta:{confidence:.75,tokens:100}, parent:"cp-d4e5f6" },
  { id:"cp-m4n5o6", ts:now-21000, status:"active", branch:"main", path:["task_intake","planning","retrieve:success"], desc:"Retry succeeded — live data retrieved", state:{revenue:"$12.5B",net_income:"$3.2B",eps:"$2.45",yoy_growth:"16%"}, meta:{confidence:.95,tokens:350}, parent:"cp-d4e5f6" },
  { id:"cp-p7q8r9", ts:now-14000, status:"active", branch:"main", path:["task_intake","planning","retrieve:success","merge:cached"], desc:"Merged cached-path for cross-validation", state:{merged:true,validated:true,data_match:"98.4%"}, meta:{confidence:.96,tokens:400}, parent:"cp-m4n5o6" },
  { id:"cp-s1t2u3", ts:now-7000, status:"active", branch:"main", path:["task_intake","planning","retrieve:success","merge:cached","summarize"], desc:"Final summary generated — task complete", state:{status:"completed",summary:"Q4 revenue $12.5B (+16% YoY), net income $3.2B, EPS $2.45"}, meta:{confidence:.97,tokens:500}, parent:"cp-p7q8r9" },
];

const BRANCHES = [
  { name:"main", count:5, current:true },
  { name:"cached-path", count:2, current:false },
];

const METRICS = { checkpoints:7, rollbacks:1, recoveries:1, branches:2, errors:1, saved:"12.4s" };

const Pill = ({children, color, bg}) => (
  <span style={{fontSize:10, padding:"2px 8px", borderRadius:10, background:bg, color, fontWeight:600, letterSpacing:".02em"}}>{children}</span>
);

const confColor = (c) => c>.9 ? C.green : c>.5 ? C.amber : C.red;
const confBg = (c) => c>.9 ? C.greenBg : c>.5 ? C.amberBg : C.redBg;
const statusIcon = (s,b,m) => s==="rolled_back"?"❌" : m?.merged_from || m?.merged ? "🔀" : b!=="main"?"🌿":"✅";

export default function AgentStateProtocolDashboard() {
  const [selected, setSelected] = useState(null);
  const [tab, setTab] = useState("tree");
  const [simStep, setSimStep] = useState(-1);
  const [simRunning, setSimRunning] = useState(false);

  const visibleCPs = simStep >= 0 ? CHECKPOINTS.slice(0, simStep + 1) : CHECKPOINTS;

  const runSim = useCallback(() => {
    setSimRunning(true);
    setSimStep(0);
    setSelected(null);
    let step = 0;
    const iv = setInterval(() => {
      step++;
      if (step >= CHECKPOINTS.length) { clearInterval(iv); setSimRunning(false); return; }
      setSimStep(step);
      setSelected(CHECKPOINTS[step]);
    }, 1200);
    setSelected(CHECKPOINTS[0]);
  }, []);

  const resetSim = () => { setSimStep(-1); setSimRunning(false); setSelected(null); };

  // Tree structure builder
  const buildTree = (cps) => {
    const nodes = {};
    const roots = [];
    cps.forEach(cp => { nodes[cp.id] = {...cp, children:[]}; });
    cps.forEach(cp => {
      if (cp.parent && nodes[cp.parent]) nodes[cp.parent].children.push(nodes[cp.id]);
      else roots.push(nodes[cp.id]);
    });
    return roots;
  };

  const renderTree = (node, depth=0, isLast=true) => {
    const isSel = selected?.id === node.id;
    const prefix = depth === 0 ? "" : "│  ".repeat(depth-1) + (isLast ? "└─ " : "├─ ");
    return (
      <div key={node.id}>
        <div onClick={()=>setSelected(node)} style={{
          display:"flex", alignItems:"center", gap:8, padding:"5px 10px", borderRadius:6, cursor:"pointer",
          background: isSel ? C.blueBg : "transparent",
          border: isSel ? `1px solid ${C.borderHi}` : "1px solid transparent",
          transition:"all .12s",
          fontFamily:"'JetBrains Mono','Fira Code',monospace", fontSize:12.5,
        }}
          onMouseEnter={e=>{if(!isSel)e.currentTarget.style.background=C.cardHover}}
          onMouseLeave={e=>{if(!isSel)e.currentTarget.style.background="transparent"}}
        >
          <span style={{color:C.dim, whiteSpace:"pre", userSelect:"none"}}>{prefix}</span>
          <span>{statusIcon(node.status, node.branch, node.meta)}</span>
          <span style={{color:C.text, flex:1}}>{node.desc.slice(0,50)}</span>
          <span style={{fontSize:10, color:C.dim, background:C.bg, padding:"2px 6px", borderRadius:3}}>{node.id.slice(3,11)}</span>
          <Pill color={confColor(node.meta.confidence)} bg={confBg(node.meta.confidence)}>{(node.meta.confidence*100).toFixed(0)}%</Pill>
        </div>
        {node.children?.map((child,i) => renderTree(child, depth+1, i===node.children.length-1))}
      </div>
    );
  };

  const trees = buildTree(visibleCPs);

  return (
    <div style={{
      minHeight:"100vh", background:C.bg, color:C.text,
      fontFamily:"'Inter','SF Pro Display',-apple-system,sans-serif",
      padding:24, maxWidth:960, margin:"0 auto",
    }}>
      {/* Header */}
      <div style={{display:"flex", alignItems:"center", justifyContent:"space-between", marginBottom:28}}>
        <div>
          <h1 style={{fontSize:26, fontWeight:700, margin:0, letterSpacing:"-0.03em", display:"flex", alignItems:"center", gap:10}}>
            <span style={{fontSize:28}}>🧠</span> AgentStateProtocol
          </h1>
          <p style={{color:C.dim, fontSize:13, margin:"4px 0 0"}}>Checkpointing & Recovery Protocol for AI Agents — Git for Thoughts</p>
        </div>
        <div style={{display:"flex", gap:8}}>
          <button onClick={simRunning ? undefined : runSim} disabled={simRunning} style={{
            padding:"8px 18px", borderRadius:8, border:"none", cursor:simRunning?"default":"pointer",
            background:simRunning?C.card:C.blue, color:"#fff", fontSize:13, fontWeight:600,
            opacity:simRunning?.6:1, transition:"all .15s",
          }}>
            {simRunning ? "⏳ Simulating..." : "▶ Run Demo"}
          </button>
          {simStep >= 0 && <button onClick={resetSim} style={{
            padding:"8px 14px", borderRadius:8, border:`1px solid ${C.border}`, cursor:"pointer",
            background:"transparent", color:C.muted, fontSize:13,
          }}>Reset</button>}
        </div>
      </div>

      {/* Metrics */}
      <div style={{display:"flex", gap:10, marginBottom:20, flexWrap:"wrap"}}>
        {[
          {label:"Checkpoints", value: simStep>=0 ? simStep+1 : METRICS.checkpoints, icon:"💾", color:C.blue},
          {label:"Rollbacks", value: simStep>=0 ? (simStep>=3?1:0) : METRICS.rollbacks, icon:"⏪", color:C.amber},
          {label:"Recoveries", value: simStep>=0 ? (simStep>=4?1:0) : METRICS.recoveries, icon:"♻️", color:C.green},
          {label:"Branches", value: simStep>=0 ? (simStep>=3?2:1) : METRICS.branches, icon:"🌿", color:C.purple},
          {label:"Errors Caught", value: simStep>=0 ? (simStep>=2?1:0) : METRICS.errors, icon:"🛡️", color:C.red},
          {label:"Time Saved", value:METRICS.saved, icon:"⚡", color:C.cyan},
        ].map(m => (
          <div key={m.label} style={{
            background:C.card, border:`1px solid ${C.border}`, borderRadius:10,
            padding:"14px 18px", flex:1, minWidth:120, transition:"all .3s",
          }}>
            <div style={{fontSize:20, marginBottom:2}}>{m.icon}</div>
            <div style={{fontSize:22, fontWeight:700, color:m.color, letterSpacing:"-0.02em"}}>{m.value}</div>
            <div style={{fontSize:11, color:C.dim, marginTop:1}}>{m.label}</div>
          </div>
        ))}
      </div>

      {/* Branches */}
      <div style={{display:"flex", gap:8, marginBottom:20, flexWrap:"wrap"}}>
        {(simStep>=0 ? (simStep>=3 ? BRANCHES : [BRANCHES[0]]) : BRANCHES).map(b => (
          <div key={b.name} style={{
            display:"flex", alignItems:"center", gap:8, padding:"7px 14px", borderRadius:8,
            background: b.current ? C.blueBg : C.card,
            border: `1px solid ${b.current ? C.borderHi : C.border}`,
          }}>
            <span style={{color: b.current ? C.blue : C.dim, fontSize:10}}>●</span>
            <span style={{color:C.text, fontWeight: b.current ? 600 : 400, fontSize:13}}>{b.name}</span>
            <span style={{fontSize:10, color:C.dim, background:C.bg, padding:"1px 6px", borderRadius:6}}>
              {simStep>=0 ? visibleCPs.filter(c=>c.branch===b.name).length : b.count} cp
            </span>
          </div>
        ))}
      </div>

      {/* Timeline bar */}
      <div style={{background:C.card, border:`1px solid ${C.border}`, borderRadius:10, padding:"14px 18px", marginBottom:20}}>
        <div style={{fontSize:11, color:C.dim, marginBottom:10, fontWeight:600, letterSpacing:".04em", textTransform:"uppercase"}}>Timeline</div>
        <div style={{display:"flex", alignItems:"center", gap:3}}>
          {visibleCPs.map((cp,i) => {
            const isSel = selected?.id === cp.id;
            const col = cp.status==="rolled_back" ? C.red : cp.meta?.merged ? C.purple : cp.branch!=="main" ? C.cyan : C.green;
            return (
              <div key={cp.id} style={{display:"flex", alignItems:"center", flex:1}}>
                <div onClick={()=>setSelected(cp)} style={{
                  width:isSel?16:12, height:isSel?16:12, borderRadius:"50%", background:col,
                  cursor:"pointer", transition:"all .15s", boxShadow: isSel ? `0 0 10px ${col}` : "none",
                  border: isSel ? `2px solid #fff` : "2px solid transparent",
                }} title={cp.desc}/>
                {i < visibleCPs.length-1 && <div style={{flex:1, height:2, background:C.border, margin:"0 2px"}}/>}
              </div>
            );
          })}
        </div>
        <div style={{display:"flex", justifyContent:"space-between", marginTop:6}}>
          <span style={{fontSize:10, color:C.dim}}>Start</span>
          <span style={{fontSize:10, color:C.dim}}>Latest</span>
        </div>
      </div>

      {/* Tabs */}
      <div style={{display:"flex", gap:2, marginBottom:16, background:C.card, borderRadius:8, padding:3, border:`1px solid ${C.border}`}}>
        {[{k:"tree",l:"🌳 Logic Tree"},{k:"history",l:"📜 History"},{k:"code",l:"💻 Usage"}].map(t => (
          <button key={t.k} onClick={()=>setTab(t.k)} style={{
            flex:1, padding:"8px 12px", borderRadius:6, border:"none", cursor:"pointer",
            background: tab===t.k ? C.blue : "transparent",
            color: tab===t.k ? "#fff" : C.muted,
            fontSize:13, fontWeight: tab===t.k ? 600 : 400, transition:"all .12s",
          }}>{t.l}</button>
        ))}
      </div>

      <div style={{display:"flex", gap:16, flexWrap:"wrap"}}>
        {/* Main panel */}
        <div style={{flex:2, minWidth:320, background:C.card, border:`1px solid ${C.border}`, borderRadius:10, padding:18}}>
          {tab === "tree" && (
            <div>
              <h3 style={{fontSize:14, fontWeight:600, margin:"0 0 12px", color:C.muted}}>Decision Tree</h3>
              {trees.map(root => renderTree(root))}
              {visibleCPs.length === 0 && <p style={{color:C.dim, textAlign:"center", padding:40}}>Press "Run Demo" to simulate an agent session</p>}
            </div>
          )}
          {tab === "history" && (
            <div>
              <h3 style={{fontSize:14, fontWeight:600, margin:"0 0 12px", color:C.muted}}>Checkpoint History (newest first)</h3>
              {[...visibleCPs].reverse().map(cp => (
                <div key={cp.id} onClick={()=>setSelected(cp)} style={{
                  display:"flex", alignItems:"center", gap:10, padding:"8px 10px", borderRadius:6,
                  cursor:"pointer", borderBottom:`1px solid ${C.border}`,
                  background: selected?.id===cp.id ? C.blueBg : "transparent",
                }}
                  onMouseEnter={e=>{if(selected?.id!==cp.id)e.currentTarget.style.background=C.cardHover}}
                  onMouseLeave={e=>{if(selected?.id!==cp.id)e.currentTarget.style.background="transparent"}}
                >
                  <span>{statusIcon(cp.status, cp.branch, cp.meta)}</span>
                  <span style={{flex:1, fontSize:13, color:C.text}}>{cp.desc.slice(0,45)}</span>
                  <Pill color={cp.branch==="main"?C.blue:C.cyan} bg={cp.branch==="main"?C.blueBg:"rgba(6,182,212,.12)"}>{cp.branch}</Pill>
                  <Pill color={confColor(cp.meta.confidence)} bg={confBg(cp.meta.confidence)}>{(cp.meta.confidence*100).toFixed(0)}%</Pill>
                </div>
              ))}
            </div>
          )}
          {tab === "code" && (
            <div>
              <h3 style={{fontSize:14, fontWeight:600, margin:"0 0 12px", color:C.muted}}>Quick Start</h3>
              <pre style={{
                background:C.bg, border:`1px solid ${C.border}`, borderRadius:8, padding:16,
                fontSize:12.5, lineHeight:1.6, overflow:"auto", color:C.muted,
                fontFamily:"'JetBrains Mono','Fira Code',monospace",
              }}>{`from agentstateprotocol import AgentStateProtocol

agent = AgentStateProtocol("my-agent")

# Save agent state (like git commit)
agent.checkpoint(
    state={"reasoning": "Analyzing query..."},
    metadata={"confidence": 0.9},
    logic_step="analysis"
)

# Something went wrong? Roll back!
agent.rollback()

# Try a different approach
agent.branch("creative-path")
agent.checkpoint(state={"approach": "lateral"})

# Auto-retry with fallback
result, cp = agent.safe_execute(
    func=risky_api_call,
    state=current_state,
    max_retries=3,
    fallback=cached_fallback
)

# Merge best result back
agent.switch_branch("main")
agent.merge("creative-path")

# View the full reasoning tree
print(agent.visualize_tree())`}</pre>
              <p style={{fontSize:12, color:C.dim, marginTop:12}}>Install: <code style={{background:C.bg, padding:"2px 8px", borderRadius:4, color:C.green}}>pip install agentstateprotocol</code></p>
            </div>
          )}
        </div>

        {/* Detail panel */}
        <div style={{flex:1, minWidth:260, background:C.card, border:`1px solid ${C.border}`, borderRadius:10, padding:18}}>
          <h3 style={{fontSize:14, fontWeight:600, margin:"0 0 14px", color:C.muted}}>
            {selected ? "Checkpoint Inspector" : "Select a Checkpoint"}
          </h3>
          {selected ? (
            <div style={{fontSize:12.5}}>
              <div style={{marginBottom:14}}>
                <div style={{color:C.dim, fontSize:11, marginBottom:3}}>ID</div>
                <code style={{color:C.blue, background:C.bg, padding:"3px 8px", borderRadius:4, fontSize:12}}>{selected.id}</code>
              </div>
              <div style={{marginBottom:14}}>
                <div style={{color:C.dim, fontSize:11, marginBottom:3}}>Description</div>
                <div style={{color:C.text}}>{selected.desc}</div>
              </div>
              <div style={{display:"flex", gap:10, marginBottom:14}}>
                <div style={{flex:1}}>
                  <div style={{color:C.dim, fontSize:11, marginBottom:3}}>Branch</div>
                  <Pill color={selected.branch==="main"?C.blue:C.cyan} bg={selected.branch==="main"?C.blueBg:"rgba(6,182,212,.12)"}>{selected.branch}</Pill>
                </div>
                <div style={{flex:1}}>
                  <div style={{color:C.dim, fontSize:11, marginBottom:3}}>Status</div>
                  <Pill
                    color={selected.status==="rolled_back"?C.red:C.green}
                    bg={selected.status==="rolled_back"?C.redBg:C.greenBg}
                  >{selected.status}</Pill>
                </div>
              </div>
              <div style={{display:"flex", gap:10, marginBottom:14}}>
                <div style={{flex:1}}>
                  <div style={{color:C.dim, fontSize:11, marginBottom:3}}>Confidence</div>
                  <div style={{display:"flex", alignItems:"center", gap:6}}>
                    <div style={{flex:1, height:6, background:C.bg, borderRadius:3, overflow:"hidden"}}>
                      <div style={{width:`${selected.meta.confidence*100}%`, height:"100%", background:confColor(selected.meta.confidence), borderRadius:3, transition:"width .3s"}}/>
                    </div>
                    <span style={{color:confColor(selected.meta.confidence), fontWeight:600, fontSize:12}}>{(selected.meta.confidence*100).toFixed(0)}%</span>
                  </div>
                </div>
                <div>
                  <div style={{color:C.dim, fontSize:11, marginBottom:3}}>Tokens</div>
                  <div style={{color:C.text, fontWeight:600}}>{selected.meta.tokens}</div>
                </div>
              </div>
              <div style={{marginBottom:14}}>
                <div style={{color:C.dim, fontSize:11, marginBottom:3}}>Logic Path</div>
                <div style={{display:"flex", gap:4, flexWrap:"wrap"}}>
                  {selected.path.map((p,i) => (
                    <span key={i}>
                      <span style={{fontSize:11, color:C.muted, background:C.bg, padding:"2px 6px", borderRadius:3}}>{p}</span>
                      {i < selected.path.length-1 && <span style={{color:C.dim, margin:"0 2px"}}>→</span>}
                    </span>
                  ))}
                </div>
              </div>
              <div>
                <div style={{color:C.dim, fontSize:11, marginBottom:3}}>State Snapshot</div>
                <pre style={{
                  background:C.bg, border:`1px solid ${C.border}`, borderRadius:6, padding:10,
                  fontSize:11, lineHeight:1.5, overflow:"auto", maxHeight:180, color:C.muted,
                  fontFamily:"'JetBrains Mono',monospace",
                }}>{JSON.stringify(selected.state, null, 2)}</pre>
              </div>
            </div>
          ) : (
            <div style={{color:C.dim, textAlign:"center", padding:"40px 20px", fontSize:13, lineHeight:1.6}}>
              Click any checkpoint in the tree, timeline, or history to inspect its full state, metadata, and reasoning path.
            </div>
          )}
        </div>
      </div>

      {/* Footer */}
      <div style={{textAlign:"center", marginTop:24, padding:"16px 0", borderTop:`1px solid ${C.border}`}}>
        <span style={{color:C.dim, fontSize:12}}>AgentStateProtocol v0.1.0 — Open Source · MIT License · </span>
        <span style={{color:C.blue, fontSize:12}}>pip install agentstateprotocol</span>
      </div>
    </div>
  );
}

