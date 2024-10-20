from flet import *

class Viewer(GestureDetector):
    def __init__(self,page,quotes,on_swipe,on_tap,quote_text,author):
        super().__init__()
        self.mouse_cursor =MouseCursor.MOVE
        self.quote_text =quote_text
        self.author =author
        self.page =page
        self.quotes =quotes
        self.current_index =0
        self.on_horizontal_drag_update =on_swipe
        self.on_tap =on_tap
        self.content=Stack(

            [
                Image(src='/home/collin/Desktop/Spark/app/assets/stary_night.jpg',
                      fit =ImageFit.COVER,
                      width =self.page.width,
                      height=self.page.height),
                Container(
                    content =Column(
                        [self.quote_text,

                        Row(controls=[Text(value ='|'),self.author,Text(value ='|')],alignment=MainAxisAlignment.END)]
                        ),
                    top =100,
                    right =30,
                    left =30
                    ),
                
            ],
            

            )
