from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'sprint',
        {
            'title': '馬拉松',
            'desc': '衝刺的距離',
            'unit': 'cm',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:sprint_one_cm'])
    ))
