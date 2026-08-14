from datetime import datetime
from Logger import DebugLogger
from CoreNanopub.CoreNanopub import CoreNanopub

# Logger
Logger = DebugLogger("full")

Logger.logger.info(f'-----\nCORE NANOPUB SERIALIZATION (run: {datetime.now()})\n-----')

# Nanopubs creation and serialization
npg = CoreNanopub().create_nanopub_graphs(sample=False)

Logger.logger.info(f'-----\nCORE NANOPUB SERIALIZATION COMPLETED at {datetime.now()}\n-----')
