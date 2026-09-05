from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'break_tools',
        {
            'title': '敗家子',
            'desc': '用壞工具的數量',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:broken'],
            [
                'minecraft:.+_axe',
                'minecraft:.+_hoe',
                'minecraft:.+_pickaxe',
                'minecraft:.+_shovel',
                'minecraft:fishing_rod',
                'minecraft:flint_and_steel',
                'minecraft:shears',
            ])
    ))
