import React from "react";
import axios from "axios";

import Homepage from "./Homepage/Homepage";

class App extends React.Component {
  state = {
    projects: []
  };

  componentDidMount() {
    axios.get("http://127.0.0.1:8000/api/").then(res => {
      this.setState({
        projects: res.data
      });
      console.log(res.data);
    });
  }

  render() {
    return (
      <>
        <main>
          <Homepage />
        </main>
      </>
    );
  }
}

export default App;
