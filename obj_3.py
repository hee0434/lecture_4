class Cat:
    color = 'red'
    #생성자 메소드
    def __init__(self , name , color):
        self.name = name
        self.color = color
    def meow(self, name):
        print('못생긴 {}'.format(name))
        print("길냥이 {}이는 색깔이 {}구요 자주 야옹~! 야옹~! 거려요".format(self.name, self.color))


gang_cat = ('미옹', '컬러플하')
jong_cat = ('태경', '똥이')

gang_cat.meow('라온')
jong_cat.meow('라온')
