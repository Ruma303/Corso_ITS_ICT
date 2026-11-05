import Libro from "./Libro";

export default function MostraLibri({ libri }) {
  return (<>
    {libri.map(e => (<Libro {...e} key={e.isbn}></Libro>
    ))}
  </>
  )
}