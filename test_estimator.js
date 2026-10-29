const fs=require('fs'),vm=require('vm'),assert=require('assert');
const {poolProbability}=require('./estimator.js');
const m=JSON.parse(fs.readFileSync(__dirname+'/model.json','utf8'));
const cases=JSON.parse(fs.readFileSync(__dirname+'/pool_model_cases.json','utf8'));
let error=0;for(const c of cases){const p=poolProbability(m,c.input);assert(p>=0&&p<=1);error=Math.max(error,Math.abs(p-c.expected));}assert(error<1e-10);
const page=fs.readFileSync(__dirname+'/index.html','utf8');
const nodes={};function el(id){return nodes[id]??=( {value:({balls:'1',foul:'NO',zone:'MIDDLE',path:'CLEAR',lowest:'2'})[id]??'',textContent:'',style:{},children:[],append(x){this.children.push(x)},addEventListener(){}})}
const ctx={document:{getElementById:el,createElement:()=>({textContent:'',children:[],append(x){this.children.push(x)}})},poolProbability,console};vm.createContext(ctx);
const scripts=[...page.matchAll(/<script>([\s\S]*?)<\/script>/g)];for(const x of scripts)vm.runInContext(x[1],ctx);
assert(/%$/.test(el('prob').textContent));assert(el('stats').children.length>8);
el('balls').value='0';el('lowest').value='4';vm.runInContext('update()',ctx);assert(el('prob').textContent==='—');
el('reset').onclick();assert(/%$/.test(el('prob').textContent));
el('foul').value='YES';el('zone').value='UNKNOWN';el('path').value='UNKNOWN';el('lowest').value='1';vm.runInContext('update()',ctx);assert(/%$/.test(el('prob').textContent));
for(const x of page.matchAll(/(?:src|href)="([^"]+)"/g)){const name=x[1];if(name.startsWith('#')||name.startsWith('http')||name.endsWith('.zip'))continue;assert(fs.existsSync(__dirname+'/'+name),'Missing asset '+name)}
console.log(`PASS: ${cases.length} Python/JavaScript probability comparisons; maximum error ${error}. Dashboard initialization, invalid input, reset, unknown/foul and local asset checks passed.`);
