# back-end

About Dataset

### Context
Melbourne real estate near RMIT University.

### Content
This is a snapshot of a dataset created by Thu Tran.

It was scraped from publicly available results posted every week from [Dwell Village](https://www.dwellstudent.com.au/melbourne/#rooms),[Domain](https://www.domain.com.au/sale/inspection-times/?ptype=apartment-unit-flat,block-of-units,duplex,free-standing,new-apartments,new-home-designs,new-house-land,pent-house,semi-detached,studio,terrace,town-house,villa&excludeunderoffer=1&keywords=rmit+university), [Zillow](https://www.zillow.com/melbourne-fl/rentals/?searchQueryState=%7B%22pagination%22%3A%7B%7D%2C%22usersSearchTerm%22%3A%22Melbourne%2C%20FL%22%2C%22mapBounds%22%3A%7B%22west%22%3A-80.93409468457031%2C%22east%22%3A-80.39439131542969%2C%22south%22%3A27.96619499260209%2C%22north%22%3A28.335500912695093%7D%2C%22regionSelection%22%3A%5B%7B%22regionId%22%3A19307%2C%22regionType%22%3A6%7D%5D%2C%22isMapVisible%22%3Atrue%2C%22filterState%22%3A%7B%22fsba%22%3A%7B%22value%22%3Afalse%7D%2C%22fsbo%22%3A%7B%22value%22%3Afalse%7D%2C%22nc%22%3A%7B%22value%22%3Afalse%7D%2C%22fore%22%3A%7B%22value%22%3Afalse%7D%2C%22cmsn%22%3A%7B%22value%22%3Afalse%7D%2C%22auc%22%3A%7B%22value%22%3Afalse%7D%2C%22fr%22%3A%7B%22value%22%3Atrue%7D%2C%22ah%22%3A%7B%22value%22%3Atrue%7D%7D%2C%22isListVisible%22%3Atrue%2C%22mapZoom%22%3A11%7D). He cleaned it well, and now it's up to you to make data analysis magic. The dataset includes Address, Type of Real estate, Suburb, Method of Selling, Rooms, Price, Real Estate Agent, Date of Sale and distance from C.B.D.

Notes on Specific Variables
+ rooms: Number of rooms
+ price: Price in dollars
+ distance: Distance from CBD
+ bathroom: Number of Bathrooms
+ Area: Land Size

### Acknowledgements
This is intended as a static (unchanging) snapshot of Melbourne Backpack. It was created in April 2022. Additionally, homes with no Price have been removed.
