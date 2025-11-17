import React, { StrictMode } from 'react'
import { createRoot } from 'react-dom/client'
import './index.css'
import App from './App.jsx'
import {App1, App2} from './App.jsx'
import Imagesetup from './Image_src.jsx'
import Toggle from './Toggle.jsx'
import { Increment } from './Toggle.jsx'
import { Reactcomponent } from './Toggle.jsx'
import Props from './Propesexample.jsx'
import Main_propexam from './propexam.jsx'
import { Main_propexam_class } from './props_with_clss.jsx'

createRoot(document.getElementById('root')).render(
  <StrictMode>
  <Main_propexam_class />
  </StrictMode>,
)
