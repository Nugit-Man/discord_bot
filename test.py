def write_bar():    
    num = 0
    while True:
        fout = open(f"count0{num}.json","w")
        fout.write("""{
        "parent": "minecraft:item/generated",
        "textures": {
            "layer0": "item/count0"""+str(num)+""""
        },
        "display": {
            "gui": {
            "translation": [
            0,
            40,
            -1
        ],
        "scale": [
            1.2,
            1,
            1.2
        ]
        },
        "firstperson_righthand": {
        "scale": [
            0,
            0,
            0
        ]
        },
        "thirdperson_righthand": {
        "scale": [
            0,
            0,
            0
        ]
        },
        "firstperson_lefthand": {
        "scale": [
            0,
            0,
            0
        ]
        },
        "thirdperson_lefthand": {
        "scale": [
            0,
            0,
            0
        ]
        }
        }
    }""")
        fout.close()
        num += 1
        if num > 10:
            break

write_bar()
for i in range(30,0,-1):
    print("""damage @s[scores={MM_Damage=""",i*5,"""..}] """,i,""" generic
scoreboard players remove @s[scores={MM_Damage=,""",i*5,""",..}] MM_Damage """,i*5,"""
""",sep="",end="")