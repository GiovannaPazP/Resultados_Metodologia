import os
import re
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import matplotlib.ticker as mticker

def analisar_resultados_sort(diretorio):
    dados = []
    regex_nome_arquivo = re.compile(r'(.+)(\w+)(\d+)\.txt')
    regex_tempo = re.compile(r'Vetor de \d+ elementos: ([\d.]+) segundos')
    regex_memoria = re.compile(r'consumo de mem[oó]ria: (\d+) bytes', re.IGNORECASE)
    nomes_legiveis = {
        "quick": "Quick (Pivô Central)", "pivo_ini_quick": "Quick (Pivô Inicial)",
        "insertion": "Insertion Sort", "bubble": "Bubble Sort", "selection": "Selection Sort"
    }

    for nome_arquivo in os.listdir(diretorio):
        if nome_arquivo.endswith('.txt'):
            match_nome = regex_nome_arquivo.match(nome_arquivo)
            if not match_nome:
                print(f"Aviso: O arquivo '{nome_arquivo}' não corresponde ao padrão esperado e será ignorado.")
                continue
            algoritmo_raw, tipo_vetor, tamanho = match_nome.groups()
            tamanho = int(tamanho)
            if tamanho == 10000000: continue
            caminho_completo = os.path.join(diretorio, nome_arquivo)
            try:
                with open(caminho_completo, 'r', encoding='utf-8') as f:
                    conteudo = f.read()
                    match_tempo = regex_tempo.search(conteudo)
                    match_memoria = regex_memoria.search(conteudo)
                    tempo = float(match_tempo.group(1)) if match_tempo else None
                    memoria = int(match_memoria.group(1)) if match_memoria else None
                    algoritmo_legivel = nomes_legiveis.get(algoritmo_raw, algoritmo_raw.capitalize())
                    dados.append({'algoritmo': algoritmo_legivel, 'tipo_vetor': tipo_vetor.capitalize(),
                                  'tamanho': tamanho, 'tempo_s': tempo, 'memoria_bytes': memoria})
            except Exception as e:
                print(f"Aviso: Ocorreu um erro ao ler o arquivo {nome_arquivo}: {e}")

    if not dados:
        print("Nenhum dado foi encontrado ou processado.")
        return

    df = pd.DataFrame(dados)
    
    algoritmos_para_tabela = sorted(df['algoritmo'].unique())
    print("--- Tabelas de Desempenho (Tempo em Segundos) ---")
    tabela_tempo = df.pivot_table(index='tamanho', columns=['algoritmo', 'tipo_vetor'], values='tempo_s')
    print(tabela_tempo.reindex(columns=algoritmos_para_tabela, level=0))
    print("\n--- Tabelas de Desempenho (Memória em Bytes) ---")
    tabela_memoria = df.pivot_table(index='tamanho', columns=['algoritmo', 'tipo_vetor'], values='memoria_bytes')
    print(tabela_memoria.reindex(columns=algoritmos_para_tabela, level=0))

    sns.set_theme(style="white")
    algoritmos_unicos = sorted(df['algoritmo'].unique())
    paleta_cores = sns.color_palette("tab10", n_colors=len(algoritmos_unicos))
    lista_estilos_linha = [(), (4, 2), (4, 2, 1, 2), (1, 2), (2, 2), (5, 5)] 
    lista_marcadores = ['o', 'X', 's', '^', 'P', 'D']
    cores_map = dict(zip(algoritmos_unicos, paleta_cores))
    dashes_map = dict(zip(algoritmos_unicos, lista_estilos_linha))
    markers_map = dict(zip(algoritmos_unicos, lista_marcadores))

    for tipo_vetor in df['tipo_vetor'].unique():
        plt.figure(figsize=(14, 8))
        dados_grafico = df[df['tipo_vetor'] == tipo_vetor]
        
        ultimo_tamanho_valido = dados_grafico.dropna(subset=['tempo_s'])['tamanho'].max()
        dados_para_ordem = dados_grafico[dados_grafico['tamanho'] == ultimo_tamanho_valido].dropna(subset=['tempo_s'])
        ordem_parcial = dados_para_ordem.sort_values(by='tempo_s', ascending=False)['algoritmo'].tolist()
        algoritmos_todos = dados_grafico['algoritmo'].unique().tolist()
        ordem_legenda = ordem_parcial + [alg for alg in algoritmos_todos if alg not in ordem_parcial]

        ax = sns.lineplot(
            data=dados_grafico, x='tamanho', y='tempo_s', hue='algoritmo',
            hue_order=ordem_legenda, palette=cores_map, dashes=dashes_map,
            markers=markers_map, style='algoritmo', markersize=9, legend='full'
        )

        for line in ax.lines:
            if line.get_label() == 'Quick (Pivô Inicial)':
                line.set_zorder(10)
                line.set_linewidth(2.5)

        ax.set_xscale('log'); ax.set_yscale('log')
        ax.xaxis.set_major_formatter(mticker.ScalarFormatter())
        ax.get_xaxis().get_major_formatter().set_scientific(False)
        ax.get_xaxis().set_minor_formatter(mticker.NullFormatter())
        ax.tick_params(axis='x', labelrotation=45)
        ax.set_title(f'Tempo de Execução vs. Tamanho da Entrada (Vetor {tipo_vetor})', fontsize=16)
        ax.set_xlabel('Tamanho da Entrada (N) - Escala Log', fontsize=12)
        ax.set_ylabel('Tempo de Execução (segundos) - Escala Log', fontsize=12)
        plt.legend(title='Algoritmo', fontsize=11)
        sns.despine()
        plt.tight_layout()
        plt.savefig(f'../dados/graficos/grafico_tempo_{tipo_vetor.lower()}_final_visivel.png')

    df_memoria = df.dropna(subset=['memoria_bytes'])
    for tipo_vetor in df_memoria['tipo_vetor'].unique():
        plt.figure(figsize=(12, 7))
        ax = sns.lineplot(
            data=df_memoria[df_memoria['tipo_vetor'] == tipo_vetor],
            x='tamanho', y='memoria_bytes', hue='algoritmo', palette=cores_map,
            dashes=dashes_map, markers=markers_map, style='algoritmo', markersize=8
        )
        ax.set_title(f'Consumo de Memória vs. Tamanho da Entrada (Vetor {tipo_vetor})', fontsize=16)
        ax.set_xlabel('Tamanho da Entrada (N)', fontsize=12)
        ax.set_ylabel('Memória Consumida (Bytes)', fontsize=12)
        ax.get_yaxis().set_major_formatter(mticker.FuncFormatter(lambda x, p: format(int(x), ',')))
        ax.get_xaxis().set_major_formatter(mticker.FuncFormatter(lambda x, p: format(int(x), ',')))
        ax.tick_params(axis='x', labelrotation=45)
        plt.legend(title='Algoritmo')
        sns.despine()
        plt.tight_layout()
        plt.savefig(f'../dados/graficos/grafico_memoria_{tipo_vetor.lower()}_final.png')

pasta_resultados = '../dados'
analisar_resultados_sort(pasta_resultados)
print("\nAnálise concluída. Tabelas foram impressas e gráficos foram salvos como arquivos .png.")
