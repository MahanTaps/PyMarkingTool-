class ScreenShotter:

    def take_screenshot(self,doc,location,filename,q_num):
        page=doc[location[1]]
        page.set_cropbox(location[0])
        pix= page.get_pixmap()
        file_title=filename+"\Question "+str(q_num)+".png"
        pix.save(file_title)
        return file_title
    
    def take_screenshots_from_batch(self,doc,location_dict,key,label):
        batch_list=[]
        i=0
        for location in location_dict[key]:
           batch_list.extend(self.take_screenshot(doc,location,label,i))
           i+=1
        return batch_list
        

    def prepare_screenshots(self,q_doc,a_doc,locations): 
        q_pics=[]
        stem_pics=[]
        a_pics=[]
        i=0
                # for location in locations['q_rects']:
        #     i+=1
        #     q_pics.extend(self.take_screenshot(q_doc,location,'Questions',i))
        # for location in locations['stem_rects']:
        #     i+=1
        #     stem_pics.extend(self.take_screenshot(q_doc,location,'QuestionStem',i))
        # for location in locations['a_rects']:
        #     i+=1
        #     a_pics.extend(self.take_screenshot(a_doc,location,'Answers',i))
        # q_pics=self.take_screenshots_from_batch(q_doc,locations,'q_rects','Questions')
        # stem_pics=self.take_screenshots_from_batch(q_doc,locations,'stem_rects','QuestionStem')
        # a_pics=self.take_screenshots_from_batch(a_doc,locations,'a_rects','Answers')
        screenshots ={
            'q_pics':self.take_screenshots_from_batch(q_doc,locations,'q_rects','Questions'),
            'stem_pics':self.take_screenshots_from_batch(q_doc,locations,'stem_rects','QuestionStem'),
            'a_pics':self.take_screenshots_from_batch(a_doc,locations,'a_rects','Answers')
        }
        return screenshots






    

