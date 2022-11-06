from mmdet.registry import DATASETS
from .coco import CocoDataset

@DATASETS.register_module()
class PlateDataset(CocoDataset):
    """Dataset for Plate"""
    
    METAINFO = {
        'CLASSES': ('plate'),
        'PALETTE': [(220, 20, 60)]
    }