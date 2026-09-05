from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'drop',
        {
            'title': '丟棄者',
            'desc': '丟棄的物品數量',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:custom','minecraft:drop'])
    ))
