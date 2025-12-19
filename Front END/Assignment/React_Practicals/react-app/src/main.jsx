import { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import Hello from './Hello.jsx';
import Example from './welcomt.jsx';
import Entername from './Greet.jsx';
import Greet from './Greet_class.jsx';
import Userdata from './UserCard.jsx';
import Counter from './Counter.jsx';
import ButtonToggle from './ButtonToggle.jsx';
import SimpleForm from './SimpleForm.jsx';
import UserloginStatus from './login_logout.jsx'
import Checkeligibillityforvote from './Check_eligibillity_for_vote.jsx';
import Fruit_map from './Fruit_map.jsx';
import DisplayUserlist from './user_with_unique_id.jsx';
import Form from './Form.jsx';
import UserList from './class_example.jsx';
import Life_cycle from './main_component.jsx';

createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Life_cycle />
  </StrictMode>,
)
