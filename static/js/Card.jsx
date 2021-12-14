'use strict';

let ParkCard = (props) => {
  function routeToDetailsPage() {
    window.location.href=`/park/${props.park_id}`
  }
  return (
      <div className="card">
      <img className="park-img" src={props.img} alt="park_img" />
      <p>{props.name}</p>
      <button type="button" onClick={routeToDetailsPage}>Park detail</button>
      </div>
  );
}

let ParkCardContainer = (props) => {
    const allParkCards = [];
    for (const currentCard of props.parkCards) {
        allParkCards.push(
        <ParkCard
          park_id={currentCard.park_id}
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

fetch('/parks.json')
    .then(response => response.json())
    .then(jsonData => {

      ReactDOM.render(<ParkCardContainer parkCards={jsonData.parks} />, document.querySelector("#all-cards"));
    })




