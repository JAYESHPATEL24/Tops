import { useContext } from "react";
import { Example } from "./create_context";

const Use_created_context = () => {
  const { user } = useContext(Example);

  return (
    <div>
      <h1>User Name: {user.name}</h1>
      <h2>User ID: {user.Id}</h2>
    </div>
  );
};

export default Use_created_context;
