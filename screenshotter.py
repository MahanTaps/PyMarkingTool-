
class ScreenShotter:
    
    def take_screenshot(page_num,rectangle,doc,q_num,filename):
        page=doc[page_num]
        page.set_cropbox(rectangle)
        pix= page.get_pixmap()
        file_title=filename+"\Question "+str(q_num)+".png"
        pix.save(file_title)
        return file_title
    

