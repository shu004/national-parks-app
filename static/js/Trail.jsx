'use strict';

function Trails() {

    const [trails, setTrails] = React.useState([]);

    React.useEffect(() => {
        const park_id = document.querySelector(".park-details-container").id
        const queryString = new URLSearchParams({park_id: park_id})

        fetch(`/gettrails.json?${queryString}`)
            .then(response => response.json())
            .then(result => {
                console.log(result)
                setTrails(result)
        });
    }, []);

    const trailList = [];

    for (const trail of trails) {
        trailList.push(<p key={trail.trail_id}>{trail.trail_name}</p>);
    }

    return <ul>{trailList}</ul>
}

ReactDOM.render(<Trails />, document.querySelector('.trails-container-react'));

