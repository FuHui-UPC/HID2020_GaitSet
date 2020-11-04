conf = {
    "WORK_PATH": "./work",
    "CUDA_VISIBLE_DEVICES": "0",
    "data": {
        'dataset_path': "dataset/CASIA-E_pre",
        'resolution': '64',
        'dataset': 'CASIA-E',
        'pid_num': 500,
        'pid_shuffle': False,
    },
    "probe": {
        'dataset_path': "dataset/test_probe_pre",
        'resolution': '64',
        'dataset': 'CASIA-E',
        'pid_num': 1,
        'pid_shuffle': False,
    },
    "gallery": {
        'dataset_path': "dataset/test_gallery_pre",
        'resolution': '64',
        'dataset': 'CASIA-E',
        'pid_num': 513,
        'pid_shuffle': False,
    },
    "model": {
        'hidden_dim': 256,
        'lr': 1e-4,
        'hard_or_full_trip': 'full',
        'batch_size': (8, 16),
        'restore_iter': 0,
        'total_iter': 200000,
        'margin': 0.2,
        'num_workers': 0,
        'frame_num': 30,
        'model_name': 'GaitSet',
    },
}
