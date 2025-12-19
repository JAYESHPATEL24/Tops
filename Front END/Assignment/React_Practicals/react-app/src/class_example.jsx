import React, { Component } from 'react';

class UserList extends Component {
  constructor(props) {
    super(props);
    this.state = {
      users: [],      
      loading: true,  
      error: null     
    };
  }

  // Lifecycle method: runs after the component is mounted
  componentDidMount() {
    fetch('https://jsonplaceholder.typicode.com/users')
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        this.setState({ users: data, loading: false });
      })
      .catch(error => {
        this.setState({ error: error.message, loading: false });
      });
  }

  render() {
    const { users, loading, error } = this.state;

    if (loading) {
      return <p>Loading data...</p>;
    }

    if (error) {
      return <p>Error: {error}</p>;
    }

    return (
      <div>
        <h2>User List</h2>
        <ul>
          {users.map(user => (
            <li key={user.id}>
              {user.name} ({user.email})
            </li>
          ))}
        </ul>
      </div>
    );
  }
}

export default UserList;