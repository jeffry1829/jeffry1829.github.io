from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'play',
        {
            'title': '成癮',
            'desc': '總遊玩時間',
            'unit': 'ticks',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:play_one_minute'])
    ))
