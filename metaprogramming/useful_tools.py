class SingletonPerUniqueParams(type):
    _instances = {}

    def __call__(cls, *args, **kwargs):
        instance_id = (cls, str(tuple(args)), str(sorted(kwargs.items())))
        if instance_id in cls._instances:
            return cls._instances[instance_id]
        instance = super(SingletonPerUniqueParams, cls).__call__(*args, **kwargs)
        cls._instances[instance_id] = instance
        return instance
