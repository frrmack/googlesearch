from googlesearch import GoogleSearch

def x_vs_y_count_match(x, y):
    """Which of the two words is used more 
    on the Internet?"""
    nx = GoogleSearch(x).count()
    ny = GoogleSearch(y).count()
    print '%s vs %s:' % (x,y)
    report = '%s wins with %i vs %i'
    if   nx > ny:
        print report % (x,nx,ny)
    elif nx < ny:
        print report % (y,ny,nx)
    else:
        print "it's a tie with %s each!" % nx
    return nx, ny

if __name__ == '__main__':

    counts = x_vs_y_count_match("color", "colour")
    
