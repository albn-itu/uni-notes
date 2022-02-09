package main

import (
	"idd.com/models"
	"database/sql"
	_ "github.com/lib/pq"
	"log"
	"fmt"
	"net/http"
)

type Env struct {
	db *sql.DB
}

func main() {
	connStr := "postgres://postgres:mysecretpassword@localhost/postgres?sslmode=disable"
	db, err := sql.Open("postgres", connStr)

	if err != nil {
		log.Fatal(err)
	}

	env := &Env{db: db}

	http.Handle("/houses", houseIndex(env))
	http.ListenAndServe(":8080", nil)
}

func houseIndex(env *Env) http.HandlerFunc {
	return func(w http.ResponseWriter, r *http.Request) {
		houses, err := models.AllCoffeHouses(env.db)
		if err != nil {
				log.Println(err)
				http.Error(w, http.StatusText(500), 500)
				return
		}

    for _, house := range houses {
      fmt.Fprintf(w, "%d, %s, %s\n", house.Id, house.Name, house.License)
    }
	}
}
