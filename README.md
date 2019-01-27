# Bidding_store
 Models:
  product model (Product)
  -contains the items begin sold and the various attributes.
  -each of the item is by one of hte users registered. a user can eb either a buyer or a seller
  Bidder
  -holds the buying information i.e user name, price etc
  
  seller
  -holds the seller information i.e minimum price they set etc.
  
  


### Person:

He’ll be able to login, register, logout

### Seller: 

He’ll be able to sell, register and accept goods

### Buyer: 

He’ll be able to buy and see the auction details

Here buyer and seller are sub classes of person.

### Seller

•	Seller can upload auction product.

•	Seller can set the starting prize of the item.

•	Seller can view the bid information for their items. 

•	Seller can bid for product.

### Buyer

•	Buyer can buy package for auction.

•	Buyer can view detail of product.

•	Buyer can bid on particular product.

•	Buyer can also modify the bidding prize.

## Models:

1. user   {person_id, first_name, last_name, address, contact, password} 
2. Seller   {selling_details}
3. Buyer   {purchase_details}
