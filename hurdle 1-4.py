# Hurdle 1
# pembuatan beberapa fungsi
# membuat fungsi belok kanan
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
# membuat fungsi loncat
def loncat():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# mulai eksekusi game
move()
loncat()
move()
loncat()
move()
loncat()
move()
loncat()
move()
loncat()
move()
loncat()

# Hurdle 2
# pembuatan beberapa fungsi
# membuat fungsi belok kanan
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
# membuat fungsi loncat
def loncat():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# mulai eksekusi game
# selama karter belum menyentuh bendera finish, maka program akan terus melakukan perulangan
while at_goal()==False: 
    move()
    loncat()


# Hurdle 3
# pembuatan beberapa fungsi
# membuat fungsi belok kanan
def turn_right():
    turn_left()
    turn_left()
    turn_left()
    
# membuat fungsi loncat
def loncat():
    turn_left()
    move()
    turn_right()
    move()
    turn_right()
    move()
    turn_left()

# mulai eksekusi game
# jika karakter belum menyentuh bendera finish, maka program akan melakukan perulangan
while at_goal()==False:
    # jika karakter mendeteksi ada tembok di depannya, maka karakter akan melakukan gerakan loncat, dan jika tidak mendeteksi tembok maka karakter akan jalan
    if wall_in_front()==True:
        loncat()
    else:
        move()

# Hurdle 4
# pembuatan beberapa fungsi
# membuat fungsi belok kanan
def turn_right():
    turn_left()
    turn_left()
    turn_left()

# eksekusi game
# program akan terus mengulang fungsi auto() jika karakter belum sampai tujuan
while at_goal()==False:
    # karakter akan belok kiri jika ada tembok di depan
    if wall_in_front()==True and wall_on_right()==True:
        turn_left()
        # karakter akan jalan jika didepan kosong
        if front_is_clear()==True:
            move()
    # karakter akan bergerak jika di depan kosong dan sebelah kanan adalah tembok
    elif wall_in_front()==False and wall_on_right()==True:
        move()
    # karakter akan belok kanan jika di sebelah kanan tidak ada tembok
    elif wall_on_right()==False:
        turn_right()
        # karakter akan bergerak jika didepan kosong
        if front_is_clear()==True:
            move()

# pembuatan beberapa fungsi
# membuat fungsi belok kanan
def turn_right():
    turn_left()
    turn_left()
    turn_left()
