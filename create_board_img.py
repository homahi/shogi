import csv
from PIL import Image


with open('board2.csv') as fin:
    cin = csv.reader(fin)
    board = [row for row in cin]

SIZE=52
canvas=Image.new('RGBA',(SIZE*9,SIZE*9),(0, 0, 0, 0))
col=0
row=0
for boardLine in board:
    col=0
    for cell in boardLine:
        cell_default_path = './img/'+cell[0]+'00'+'.png'
        img=Image.open(cell_default_path,'r')
        if cell!='9' and cell[1]=='1':
            img = img.transpose(Image.ROTATE_180)
        canvas.paste(img,(col*SIZE,row*SIZE))
        print(col,row,cell_default_path)
        col+=1
    row+=1
canvas.save('c.png','PNG',quality=100,optimize=True)