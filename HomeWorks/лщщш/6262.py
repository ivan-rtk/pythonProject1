__name__ == '__main__':
    mik = Student("Mikhail", "Sergeevich", "Fedko", Path('lessons.csv'))
    print(mik)
    mik.new_estimate("русский язык", 5)
    mik.new_estimate("сопротивление материалов", 5)
    mik.new_estimate("физика", 2)
    mik.new_estimate("физика", 4)
    mik.new_estimate("математика", 5)
    mik.new_estimate("русский язык", 2)
    mik.new_estimate("сопротивление материалов", 3)
    mik.new_estimate("физика", 5)
    mik.new_estimate("физика", 2)
    mik.new_estimate("математика