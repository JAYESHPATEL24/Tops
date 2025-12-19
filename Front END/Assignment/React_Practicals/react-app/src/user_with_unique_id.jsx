function DisplayUserlist() {
    const users = [
        { id: 1, name: 'Raju' },
        { id: 2, name: 'BabuRao' },
        { id: 3, name: 'Shyam' },
    ];

        return (
            <div>
            <h2>User List</h2>
            <ul>
                {users.map((user) => (
                <li key={user.id}>{user.name}</li>
                ))}
            </ul>
            </div>
        );
    }

export default DisplayUserlist;