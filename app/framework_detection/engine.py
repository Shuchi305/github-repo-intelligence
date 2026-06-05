"""Framework detection engine"""

class DetectionEngine:
    def __init__(self):
        self.detectors = []

    def register(self, detector):
        self.detectors.append(detector)

    def detect(self, repo_path: str):
        results = {}
        for d in self.detectors:
            results[d.__class__.__name__] = d.detect(repo_path)
        return results
