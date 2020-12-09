
from ._base_metric import _BaseMetric
from .. import _timing


class Count(_BaseMetric):
    """Class which simply counts the number of tracker and gt detections and ids."""
    def __init__(self):
        super().__init__()
        self.integer_fields = ['Dets', 'GT_Dets', 'IDs', 'GT_IDs']
        self.fields = self.integer_fields
        self.summary_fields = self.fields

    @_timing.time
    def eval_sequence(self, data):
        """Returns counts for one sequence"""
        # Get results
        res = {'Dets': data['num_tracker_dets'],
               'GT_Dets': data['num_gt_dets'],
               'IDs': data['num_tracker_ids'],
               'GT_IDs': data['num_gt_ids']}
        return res

    def combine_sequences(self, all_res):
        """Combines metrics across all sequences"""
        res = {}
        for field in self.integer_fields:
            res[field] = self._combine_sum(all_res, field)
        return res