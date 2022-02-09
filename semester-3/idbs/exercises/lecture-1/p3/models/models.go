package models

import (
	"database/sql"
)

type CoffeeHouse struct {
	Id int64
	Name string
	License string
}

func AllCoffeHouses(db *sql.DB) ([]CoffeeHouse, error) {
	rows, err := db.Query("SELECT * FROM lecture1.coffee_houses")
	if err != nil {
		return nil, err
	}
	defer rows.Close()

	var houses []CoffeeHouse

	for rows.Next() {
		var house CoffeeHouse
		if err := rows.Scan(&house.Id, &house.Name, &house.License); err != nil {
			return nil, err
		}

		houses = append(houses, house)
	}

	return houses, nil
}
