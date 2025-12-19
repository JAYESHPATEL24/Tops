import React from "react";
import useCustomHook from "./custom_hook_example"; 
export default function AnotherHookExample() {
  const [value, toggle] = useCustomHook(true);

  return (
    <div>
      <button onClick={() => toggle()}>
        Please Click Me!
      </button>

      {value ? <h1>Welcome</h1> : <h1>Good Bye</h1>}
    </div>
  );
}
