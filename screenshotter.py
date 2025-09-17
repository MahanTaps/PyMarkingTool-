
class ScreenShotter:
    
    def take_screenshot(doc,location,q_num,filename):
        page=doc[location[1]]
        page.set_cropbox(location[0])
        pix= page.get_pixmap()
        file_title=filename+"\Question "+str(q_num)+".png"
        pix.save(file_title)
        return file_title
    

