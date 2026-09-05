from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_cobweb',
        {
            'title': '...煩死了！',
            'desc': '清除過的蜘蛛網的數量',
            'unit': 'int',
        },
        mcstats.StatReader(['minecraft:mined','minecraft:cobweb'])
    ))
