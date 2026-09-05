from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'interact_lectern',
        {
            'title': '講師',
            'desc': '使用講台的次數',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:interact_with_stonecutter']),
        1921 # lecterns usable since 19w02a
    ))
