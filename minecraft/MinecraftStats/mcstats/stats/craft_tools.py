from mcstats import mcstats

mcstats.registry.append(
    mcstats.MinecraftStat(
        'craft_tools',
        {
            'title': '工作坊',
            'desc': '製造的工具數量',
            'unit': 'int',
        },
        mcstats.StatSumMatchReader(
            ['minecraft:crafted'],
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
