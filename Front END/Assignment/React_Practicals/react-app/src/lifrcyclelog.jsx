import React, { Component } from "react";

class LifecycleLogger extends Component {
  componentDidUpdate(prevProps, prevState) {
    console.log("Component updated");

    // Optional: check what changed
    if (prevProps.count !== this.props.count) {
      console.log("Count prop changed from", prevProps.count, "to", this.props.count);
    }
  }

  componentWillUnmount() {
    console.log("Component is unmounting");
  }

  render() {
    return (
      <div>
        <h2>Lifecycle Logger</h2>
        <p>Count: {this.props.count}</p>
      </div>
    );
  }
}

export default LifecycleLogger;