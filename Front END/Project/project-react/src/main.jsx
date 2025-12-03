import React, { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import "bootstrap/dist/css/bootstrap.min.css";

// import './index.css'
import App from './App.jsx'
import {App1, App2} from './App.jsx'
import Imagesetup from './Image_src.jsx'
import Toggle from './Toggle.jsx'
import { Increment } from './Toggle.jsx'
import { Reactcomponent } from './Toggle.jsx'
import Props from './Propesexample.jsx'
import Main_propexam from './propexam.jsx'
import { Main_propexam_class } from './props_with_clss.jsx'
import Timer from './usestatesexample.jsx'
import Card from './caedexample.jsx'
import Carddata from './cardexA.jsx'
import Tabledata from './tableform.jsx'
import UseRed from './usereduceexample.jsx'
import UseDays from './switchdays.jsx'
import Form from './formexample.jsx'
import CheckboxExample from './checkboxexample.jsx'
import FullFormexample from './FullFormexample.jsx'
import Calculater from './calculater.jsx'


createRoot(document.getElementById('root')).render(
  <StrictMode>
    <Calculater />
  </StrictMode>,
)