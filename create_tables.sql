CREATE TABLE `Flower`
(
  `id` int AUTO_INCREMENT PRIMARY KEY,
  `name` varchar(255) NOT NULL,
  `color` varchar(255) NOT NULL,
  `current_price` int NOT NULL,
  `available` int NOT NULL,
  INDEX (id),
  CONSTRAINT UNIQUE (`color`, `name`)
);

CREATE TABLE `OrderFlower`
(
  `order_id` int,
  `flower_id` int,
  `quantity` int NOT NULL
);

CREATE TABLE `Gift`
(
  `id` int AUTO_INCREMENT PRIMARY KEY,
  `name` varchar(255) UNIQUE NOT NULL,
  `current_price` int NOT NULL,
  `available` int NOT NULL
);

CREATE TABLE `OrderGift`
(
  `order_id` int,
  `gift_id` int,
  `quantity` int NOT NULL
);

CREATE TABLE `Merchant`
(
  `id` int AUTO_INCREMENT PRIMARY KEY,
  `info_id` int,
  `added_at` datetime NOT NULL,
  `access_level` int NOT NULL
);

CREATE TABLE `Order`
(
  `id` int AUTO_INCREMENT PRIMARY KEY,
  `merchant_id` int,
  `completed_at` datetime,
  `user_id` int,
  `total_sum` int
);

CREATE TABLE `User`
(
  `id` int AUTO_INCREMENT PRIMARY KEY,
  `info_id` int,
  `added_at` datetime NOT NULL,
  `discount_category` int NOT NULL,
  `invited_by` int
);

CREATE TABLE `PersonData`
(
  `id` int AUTO_INCREMENT PRIMARY KEY,
  `first_name` varchar(255) NOT NULL,
  `last_name` varchar(255),
  `birth_date` date NOT NULL,
  `email` varchar(255) UNIQUE,
  `mobile` bigint UNIQUE,
  `gender` varchar(1)
);

ALTER TABLE `OrderFlower` ADD FOREIGN KEY (`order_id`) REFERENCES `Order` (`id`);

ALTER TABLE `OrderFlower` ADD FOREIGN KEY (`flower_id`) REFERENCES `Flower` (`id`);

ALTER TABLE `OrderGift` ADD FOREIGN KEY (`order_id`) REFERENCES `Order` (`id`);

ALTER TABLE `OrderGift` ADD FOREIGN KEY (`gift_id`) REFERENCES `Gift` (`id`);

ALTER TABLE `Merchant` ADD FOREIGN KEY (`info_id`) REFERENCES `PersonData` (`id`);

ALTER TABLE `Order` ADD FOREIGN KEY (`merchant_id`) REFERENCES `Merchant` (`id`);

ALTER TABLE `Order` ADD FOREIGN KEY (`user_id`) REFERENCES `User` (`id`);

ALTER TABLE `User` ADD FOREIGN KEY (`info_id`) REFERENCES `PersonData` (`id`);

ALTER TABLE `User` ADD FOREIGN KEY (`invited_by`) REFERENCES `Merchant` (`id`);
