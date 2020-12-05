class BaseDataLoader:
    def __init__(self, path: str, config=None):
        """Base class for dataloaders"""
        self.path = path
        self.config = config

    def __iter__(self):
        """Iterate over samples"""
        raise NotImplementedError

    def _valid_sample(self, sample):
        """Any logic for determining if a sample should be yielded in iteration
        based on the config, or other parameters"""
        raise NotImplementedError

    def process(self):
        """Run the iterator and store all samples and labels on the object"""
        logger.info(f"Processing {self}")
        self.samples = [s for s in iter(self)]
        self.labels = None

    @classmethod
    def get_batch_cls(cls):
        """For getting a handle on the necessary batch definition"""
        raise NotImplementedError

    def get_batches(self, batch_size: int, device="cpu") -> list:
        """Returns the batches"""
        raise NotImplementedError
