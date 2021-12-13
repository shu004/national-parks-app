'use strict';


fetch('/parks.json')
    .then(response => response.json())
    .then(jsonData => {
        let parkCards = []
        for (const park of jsonData.parks){
            parkCards.push(park)

            function ParkCard(props) {
              return (
                  <div className="card">
                  <img className="park-img" src={props.img} alt="park_img" />
                  <p>{props.name}</p>
                  </div>
              );
            }

            function ParkCardContainer() {
                const allParkCards = [];
                for (const currentCard of parkCards) {
                    allParkCards.push(
                    <ParkCard
                      img={currentCard.img}
                      name={currentCard.park_name}
                    />
                  );
                }
                return (
                  <React.Fragment>
                    {allParkCards}
                  </React.Fragment>
                );
              }

            ReactDOM.render(<ParkCardContainer />, document.querySelector("#all-cards"));
        }
    })





