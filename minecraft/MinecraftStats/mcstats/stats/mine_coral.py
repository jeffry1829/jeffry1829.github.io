from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'mine_coral',
        {
            'title': '珊瑚收集家',
            'desc': '挖過的珊瑚的數量',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:mined'],[
                'minecraft:.+_coral',
                'minecraft:.+_coral_block',
                'minecraft:.+_coral_fan',
                'minecraft:.+_coral_wall_fan',
            ]
        ),
        1473 # corals added in 18w10a
    ))
