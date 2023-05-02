insert into
  inventory_category (id, name)
values
  (1, 'Kitchenware'),
  (2, 'Cookware'),
  (3, 'Jewelry'),
  (4, 'Appliances'),
  (5, 'Books'),
  (6, 'Electronics'),
  (7, 'Art'),
  (8, 'Food'),
  (9, 'Tools'),
  (10, 'Toys'),
  (11, 'Shoes'),
  (12, 'Clothing'),
  (13, 'Sports');

insert into
  inventory_storagetype (id, name, date_organized, location_id)
values
  (1, 'Pantry','2020-07-07 00:00:00', 3),
  (2, 'Cabinet','2020-07-07 00:00:00', 5),
  (3, 'Jewelry Box','2020-07-07 00:00:00', 2),
  (4, 'Closet','2020-07-07 00:00:00', 4),
  (5, 'Bookshelf','2020-07-07 00:00:00', 2);

insert into
  inventory_location (id, name)
values
  (1, 'Kitchen'),
  (2, 'Dining Room'),
  (3, 'Bedroom'),
  (4, 'Living Room'),
  (5, 'Study');

insert into
  inventory_object (
    id,
    name,
    quantity,
    description,
    last_updated,
    storage_type_id,
    category_id,
    location_id
  )
values
  (
    1, 'lamp', 3, 'Praesent id massa id nisl venenatis lacinia.', '2020-07-07 00:00:00', 4, 13, 5
  ),
  (
    2, 'bed', 2, 'Duis aliquam convallis nunc. Proin at turpis a pede posuere nonummy.', '2020-07-07 00:00:00', 3, 11, 4
  ),
  (
    3, 'fridge', 4, 'Aenean sit amet justo. Morbi ut odio.', '2021-04-05 00:00:00', 3, 11, 2
  ),
  (
    4, 'sofa', 1, 'Suspendisse potenti.', '2020-07-20 00:00:00', 3, 7, 2
  ),
  (
    5, 'dishwasher', 3, 'Phasellus id sapien in sapien iaculis congue. Vivamus metus arcu, adipiscing molestie, hendrerit at, vulputate vitae, nisl.', '2020-08-18 00:00:00', 3, 7, 5
  ),
  (
    6, 'picture', 6, 'In hac habitasse platea dictumst.', '2020-10-25 00:00:00', 2, 9, 3
  ),
  (
    7, 'rug', 2, 'Vestibulum ante ipsum primis in faucibus orci luctus et ultrices posuere cubilia Curae; Nulla dapibus dolor vel est.', '2020-08-08 00:00:00', 2, 7, 2
  ),
  (
    8, 'microwave', 1, 'Nulla suscipit ligula in lacus.', '2021-06-03 00:00:00', 4, 7, 5
  ),
  (
    9, 'stove', 1, 'Morbi a ipsum. Integer a nibh.', '2021-03-03 00:00:00', 3, 7, 5
  ),
  (
    10, 'dryer', 1, 'Etiam faucibus cursus urna. Ut tellus.', '2021-04-18 00:00:00', 5, 9, 4
  ),
  (
    11, 'mirror', 1, 'Morbi non quam nec dui luctus rutrum. Nulla tellus.', '2021-01-19 00:00:00', 1, 7, 3
  ),
  (
    12, 'wine', 1, 'Nullam molestie nibh in lectus. Pellentesque at nulla.', '2020-12-28 00:00:00', 1, 9, 5
  ),
  (
    13, 'beer', 5, 'Aenean sit amet justo. Morbi ut odio.', '2020-07-07 00:00:00', 4, 11, 5
  ),
  (
    14, 'hat', 4, 'Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl. Nunc rhoncus dui vel sem.', '2020-08-29 00:00:00', 2, 3, 5
  ),
  (
    15, 't-shirt', 8, 'Nunc rhoncus dui vel sem.', '2020-07-25 00:00:00', 1, 9, 4
  ),
  (
    16, 'computer', 3, 'Vestibulum rutrum rutrum neque. Aenean auctor gravida sem.', '2020-07-16 00:00:00', 3, 6, 4
  ),
  (
    17, 'speaker', 8, 'Donec ut dolor.', '2021-03-05 00:00:00', 4, 2, 1
  ),
  (
    18, 'tennis_shoes', 3, 'Suspendisse accumsan tortor quis turpis. Sed ante.', '2020-07-26 00:00:00', 1, 2, 4
  ),
  (
    19, 'table', 5, 'Fusce posuere felis sed lacus. Morbi sem mauris, laoreet ut, rhoncus aliquet, pulvinar sed, nisl.', '2021-05-14 00:00:00', 5, 5, 5
  ),
  (
    20, 'washing machine', 2, 'Aenean fermentum. Donec ut mauris eget massa tempor convallis.', '2020-08-12 00:00:00', 3, 4, 3
  );