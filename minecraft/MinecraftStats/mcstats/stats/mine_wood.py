from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_wood',
        {
            'title': '伐木機',
            'desc': '砍過的木頭數量',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:mined'],['minecraft:.+_log'])
    ))
