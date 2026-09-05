from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'time_since_sleep',
        {
            'title': '失眠症',
            'desc': '距離上次睡覺時間',
            'unit': 'ticks',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:time_since_rest'])
    ))
