from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'time_since_death',
        {
            'title': '生存家',
            'desc': '距離上次死亡時間',
            'unit': 'ticks',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:time_since_death'])
    ))
