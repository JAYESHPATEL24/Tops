import { useState } from "react";

function useCustomHook(defaultValue) {
  const [value, setValue] = useState(defaultValue);

  const toggle = (val) => {
    if (typeof val !== "boolean") {
      setValue(!value); 
    } else {
      setValue(val); 
    }
  };

  return [value, toggle]; 
}

export default useCustomHook;
