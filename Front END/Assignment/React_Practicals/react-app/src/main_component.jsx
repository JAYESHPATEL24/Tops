import React, { Component } from "react";
import LifecycleLogger from "./lifrcyclelog.jsx";

class Life_cycle extends Component {
  state = {
    count: 0,
    show: true
  };

  render() {
    return (
      <div>
        <button onClick={() => this.setState({ count: this.state.count + 1 })}>
          Update Count
        </button>

        <button onClick={() => this.setState({ show: !this.state.show })}>
          Toggle Component
        </button>

        {this.state.show && <LifecycleLogger count={this.state.count} />}
      </div>
    );
  }
}

export default Life_cycle;
