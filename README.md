# vectors2vw

Program for vector set converting to dataset in [Vawpal Wabbit](https://github.com/JohnLangford/vowpal_wabbit) format.

## Input
Program input is path to folder which contains files with vectors in JSON format (JSON array).

Folder nesting can be any:
- vectors
  - vectors_group1
    - vectors_subgroup1
      - vector1.json
      - vector2.json
  - vectors_group2
    - vector3.json
    - vector4.json

File content example:
```
[4, 0, 0, 11, 0, 0, 0, 12, 0, 0, 0, 0, 65, 4, 0, 0, 0, 0, 0, 91, 0, 1, 0, 0, 0, 0, 0, 0, 45, 0, 0, 103, 0, 0, 0, 0, 0, 9, 3]
```

## Output

Program output is .vw file with dataset in Vawpal Wabbit format.

As the vectors are processed, the program appends the representation of these vectors to the file in Vawpal Wabbit format.

Output example (.vw file):
```
1 |n 1137:1 1142:1 1207:1 1209:1 1211:1 1212:1 1253:1 1256:1 1258:1 
2 |n 12712:7 12717:1 12912:6 12960:6 13004:6 13053:1 13072:5 66158:1.6923076923076923 66164:1 66170:1
3 |n 8084:8 8085:2 8094:12 8122:2 8145:1 8147:3 8148:3 8290:1 8865:4 8907:2 8910:2 66170:1 66205:2
4 |n 17661:3 17663:4 24198:3 26307:1 27008:1 27023:2 27035:1 27050:1 27061:4 27064:1 27073:3 27074:1 27079:2 27367:3 27369:4 27819:3 28167:5 28321:1 28322:1 28523:2 28573:1 66158:1.6875 66170:1 66185:1
```

## Example of use

```
python3 main.py -i ./vectors -o dataset.vw
```

Program arguments:
* **-i**, **--input_folder**: input folder with vectors (in JSON format);
* **-o**, **--output_file**: output file with dataset in Vawpal Wabbit format.
