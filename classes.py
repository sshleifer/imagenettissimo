class ClassFolders:
    imagenette = [
        'n01440764',
        'n02102040',
        'n02979186',
        'n03000684',
        'n03028079',
        'n03394916',
        'n03417042',
        'n03425413',
        'n03445777',
        'n03888257',
    ]

    imagewoof = [
        # TODO
    ]

    @staticmethod
    def from_indices(indices, woof=False):
        classes = []
        for i in indices:
            if woof:
                classes.append(ClassFolders.imagewoof[i])
            else:
                classes.append(ClassFolders.imagenette[i])
        return classes
