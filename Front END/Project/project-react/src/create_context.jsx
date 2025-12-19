import { createContext } from "react";

export const Example = createContext();

const Create_context = ({ children }) => {
  const user = {
    name: "Jayesh",
    Id: 101,
  };

  return (
    <Example.Provider value={{ user }}>
      {children}
    </Example.Provider>
  );
};

export default Create_context;
